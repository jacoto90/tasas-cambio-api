from flask import Flask, jsonify

app = Flask(__name__)

# Datasets
transacciones = [
    { "sku": "T2006", "amount": "10.00", "currency": "USD" },
    { "sku": "M2007", "amount": "34.57", "currency": "CAD" },
    { "sku": "R2008", "amount": "17.95", "currency": "USD" },
    { "sku": "T2006", "amount": "7.63", "currency": "EUR" },
    { "sku": "B2009", "amount": "21.23", "currency": "USD" }
]

tasas_de_cambio = [
    { "from": "EUR", "to": "USD", "rate": "1.359" },
    { "from": "CAD", "to": "EUR", "rate": "0.732" },
    { "from": "USD", "to": "EUR", "rate": "0.736" },
    { "from": "EUR", "to": "CAD", "rate": "1.366" }
]

@app.route('/tasas', methods=['GET'])
def obtener_todas_las_tasas():
    return jsonify(tasas_de_cambio)

@app.route('/tasa/<string:codigo>', methods=['GET'])
def obtener_tasa_por_codigo(codigo):
    tasas_directas = [tasa for tasa in tasas_de_cambio if tasa["to"] == codigo]
    if tasas_directas:
        return jsonify(tasas_directas)
    
    # Búsqueda indirecta
    for tasa in tasas_de_cambio:
        tasa_indirecta = next((t for t in tasas_de_cambio if t["from"] == tasa["to"] and t["to"] == codigo), None)
        if tasa_indirecta:
            tasa_combinada = float(tasa["rate"]) * float(tasa_indirecta["rate"])
            return jsonify({
                "from": tasa["from"],
                "to": codigo,
                "rate": str(tasa_combinada)
            })
    
    return jsonify({"error": "No se encontró la tasa de cambio para el código proporcionado"}), 404

@app.route('/transacciones/<string:codigo>', methods=['GET'])
def obtener_transacciones_por_moneda(codigo):
    transacciones_filtradas = [trans for trans in transacciones if trans["currency"] == codigo]
    if not transacciones_filtradas:
        return jsonify({"error": "No se encontraron transacciones para el código de moneda proporcionado"}), 404
    return jsonify(transacciones_filtradas)

@app.route('/transacciones/<string:sku>/<string:codigo_moneda>', methods=['GET'])
def obtener_transacciones_por_sku_y_moneda(sku, codigo_moneda):
    transacciones_filtradas = [trans for trans in transacciones if trans["sku"] == sku and trans["currency"] == codigo_moneda]
    if not transacciones_filtradas:
        return jsonify({"error": "No se encontraron transacciones para el SKU y código de moneda proporcionados"}), 404
    return jsonify(transacciones_filtradas)

if __name__ == '__main__':
    app.run(debug=True)
