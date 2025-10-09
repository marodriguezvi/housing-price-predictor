from typing import Annotated
from pydantic import BaseModel, Field
from ..utils.constant import HOUSE_INPUT_DESCRIPTIONS


class HouseInput(BaseModel):
    """Input schema for housing price prediction."""

    CRIM: Annotated[
        float, Field(ge=0, description=HOUSE_INPUT_DESCRIPTIONS["crim"])
    ]
    ZN: Annotated[
        float, Field(ge=0, description=HOUSE_INPUT_DESCRIPTIONS["zn"])
    ]
    INDUS: Annotated[
        float, Field(ge=0, description=HOUSE_INPUT_DESCRIPTIONS["indus"])
    ]
    CHAS: Annotated[
        int, Field(ge=0, le=1, description=HOUSE_INPUT_DESCRIPTIONS["chas"])
    ]
    NOX: Annotated[
        float, Field(gt=0, le=1, description=HOUSE_INPUT_DESCRIPTIONS["nox"])
    ]
    RM: Annotated[
        float, Field(gt=0, description=HOUSE_INPUT_DESCRIPTIONS["rm"])
    ]
    AGE: Annotated[
        float, Field(ge=0, description=HOUSE_INPUT_DESCRIPTIONS["age"])
    ]
    DIS: Annotated[
        float, Field(gt=0, description=HOUSE_INPUT_DESCRIPTIONS["dis"])
    ]
    RAD: Annotated[
        int, Field(ge=1, description=HOUSE_INPUT_DESCRIPTIONS["rad"])
    ]
    TAX: Annotated[
        float, Field(gt=0, description=HOUSE_INPUT_DESCRIPTIONS["tax"])
    ]
    PTRATIO: Annotated[
        float, Field(gt=0, description=HOUSE_INPUT_DESCRIPTIONS["ptratio"])
    ]
    B: Annotated[float, Field(ge=0, description=HOUSE_INPUT_DESCRIPTIONS["b"])]
    LSTAT: Annotated[
        float,
        Field(ge=0, description=HOUSE_INPUT_DESCRIPTIONS["lstat"]),
    ]
