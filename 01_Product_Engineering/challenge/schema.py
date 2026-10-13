"""RFQ Agent, step 1: pick vendors to send an RFQ to.

In:   part number, condition, quantity
Out:  a ranked list of vendors whose ILS listing matches, each with what they list
      or no answer, with the reason, when no listing matches
"""

from typing import Literal

from pydantic import BaseModel, Field, model_validator

# Condition codes as they exist in AvSight, minus NQ.
ConditionCode = Literal[ "FN", "NE", "NS"]

# answered        at least one vendor lists this PN in this condition and quantity -> use the list as is
# low_confidence  vendors exist, but every one is a near match, meaning short on quantity or a different condition. -> show the list with the caveat
# no_answer       nothing usable in the listings, or there are no vendors available  -> route to a buyer
Status = Literal["answered", "low_confidence", "no_answer"]


class Request(BaseModel):
    """What the buyer or upstream system hands in."""

    part_number: str = Field(min_length=1, description="The PN to source")
    condition: ConditionCode = Field(description="Condition being requested")
    quantity: int = Field(gt=0, description="Units needed")
    max_vendors: int = Field(default=5, ge=1, le=20, description="Most vendors to return")


class VendorMatch(BaseModel):
    """One vendor worth sending the RFQ to, with the listing that justifies it."""

    vendor_name: str = Field(min_length=1, description="Vendor name, exactly as in the listing")
    part_number_listed: str = Field(min_length=1, description="PN on the vendor's listing")
    condition_listed: str = Field(min_length=1, description="Condition on the vendor's listing")
    quantity_available: int = Field(ge=0, description="Quantity on the vendor's listing")
    reason: str = Field(min_length=1, description="One sentence: why this vendor, and any mismatch")


class Response(BaseModel):
    """What comes back."""

    status: Status
    vendors: list[VendorMatch] = Field(
        default_factory=list, description="Ranked best first; empty only when status is no_answer"
    )
    caveat: str | None = Field(
        default=None, description="What the buyer should know before sending; required for low_confidence"
    )
    no_answer_reason: str | None = Field(
        default=None, description="Why no vendor could be recommended; required for no_answer"
    )

    @model_validator(mode="after")
    def _status_matches_payload(self) -> "Response":
        if self.status == "no_answer":
            if self.vendors:
                raise ValueError("no_answer must not list vendors")
            if not self.no_answer_reason:
                raise ValueError("no_answer requires no_answer_reason")
        else:
            if not self.vendors:
                raise ValueError(f"{self.status} requires at least one vendor")
            if self.status == "low_confidence" and not self.caveat:
                raise ValueError("low_confidence requires a caveat")
        return self


def solve(request: Request) -> Response:
    """Find the vendors on ILS worth sending an RFQ to, for one part.

    A vendor is an exact match when its listing has the requested PN and condition and quantity.
    Vendors listing a different condition or fewer units than requested are near matches.
    Nothing usable in the listings, or there are no vendors available, that is no answer.

    """
    raise NotImplementedError("implement against this signature")