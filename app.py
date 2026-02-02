import os
from flask import Flask, request, jsonify
from formulas import (
    calc_plastic_waste_footwear,
    calc_sanitary_waste_stationeries
)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    # Optional: avoids 404 when someone opens base URL
    return jsonify({"service": "impact_api", "status": "running"})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"ok": True})


@app.route("/calc/plastic_waste_footwear", methods=["POST"])
def api_plastic_waste_footwear():
    data = request.get_json(silent=True) or {}

    waste_quantity = float(data.get("waste_quantity", 0))
    electricity_used = float(data.get("electricity_used", 0))
    collection_distance = float(data.get("collection_distance", 0))

    outputs = calc_plastic_waste_footwear(
        waste_quantity=waste_quantity,
        electricity_used=electricity_used,
        collection_distance=collection_distance
    )

    return jsonify({
        "out_1": outputs.out_1,
        "out_2": outputs.out_2,
        "out_3": outputs.out_3,
        "out_4": outputs.out_4
    })


@app.route("/calc/sanitary_waste_stationeries", methods=["POST"])
def api_sanitary_waste_stationeries():
    data = request.get_json(silent=True) or {}

    waste_quantity = float(data.get("waste_quantity", 0))
    processing_energy = float(data.get("processing_energy", 0))
    transport_distance = float(data.get("transport_distance", 0))

    outputs = calc_sanitary_waste_stationeries(
        waste_quantity=waste_quantity,
        processing_energy=processing_energy,
        transport_distance=transport_distance
    )

    return jsonify({
        "out_1": outputs.out_1,
        "out_2": outputs.out_2,
        "out_3": outputs.out_3,
        "out_4": outputs.out_4
    })


if __name__ == "__main__":
    # ✅ Render uses PORT env variable
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)



