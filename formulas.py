from dataclasses import dataclass


@dataclass
class Outputs:
    out_1: float
    out_2: float
    out_3: float
    out_4: float


def calc_plastic_waste_footwear(
    waste_quantity: float,
    electricity_used: float,
    collection_distance: float
) -> Outputs:
    """
    Tool 1: Plastic waste -> Footwear

    Replace the placeholder logic with your REAL Excel-equivalent formulas.
    Keep this file PURE: only calculations, no Flask, no Bubble.
    """

    # ---- PLACEHOLDER LOGIC (replace later) ----
    out_1 = waste_quantity * 10
    out_2 = electricity_used * 0.2
    out_3 = collection_distance * 5
    out_4 = out_1 + out_2 + out_3
    # ------------------------------------------

    return Outputs(out_1=out_1, out_2=out_2, out_3=out_3, out_4=out_4)


def calc_sanitary_waste_stationeries(
    waste_quantity: float,
    processing_energy: float,
    transport_distance: float
) -> Outputs:
    """
    Tool 2: Sanitary waste -> Stationeries

    Placeholder for now. We'll plug real formulas later.
    """

    # ---- PLACEHOLDER LOGIC (replace later) ----
    out_1 = waste_quantity * 8
    out_2 = processing_energy * 0.3
    out_3 = transport_distance * 4
    out_4 = out_1 + out_2 + out_3
    # ------------------------------------------

    return Outputs(out_1=out_1, out_2=out_2, out_3=out_3, out_4=out_4)

