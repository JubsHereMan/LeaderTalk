from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Carregar o modelo salvo
model_file_path = "classification.pkl"  # Certifique-se de que este arquivo exista
model = joblib.load(model_file_path)

# Carregar o LabelEncoder para o resultado
resultado_encoder_path = "resultado_encoder.pkl"  # Certifique-se de salvar o LabelEncoder
resultado_encoder = joblib.load(resultado_encoder_path)

# Codificadores de variáveis categóricas para entrada
label_encoders = {
    "rankMissao": {"D": 5, "C": 4, "B": 3, "A": 2, "S": 1},  # Exemplo de mapeamento
}

# Função para pré-processar os dados
def preprocess_input(data):
    try:
        # Extrair os valores do JSON enviado
        nivel_jogador = float(data.get("NivelJogador", 1))  # Default para nível 1
        rank_missao = label_encoders["rankMissao"].get(data.get("rankMissao", "D"), 5)  # Default para "D"

        # Calcular as features derivadas (success_chance e tempoEstimado)
        success_chance = nivel_jogador / rank_missao
        tempo_estimado = max(1, 10 - success_chance + np.random.normal(0, 1))

        # Exibir valores processados para debug
        print(f"Dados processados: nivelJogador={nivel_jogador}, rankMissao={rank_missao}, "
              f"success_chance={success_chance}, tempoEstimado={tempo_estimado}")

        # Retornar as features no formato esperado pelo modelo
        return np.array([nivel_jogador, rank_missao, success_chance, tempo_estimado]).reshape(1, -1)
    except Exception as e:
        raise ValueError(f"Erro no pré-processamento dos dados: {str(e)}")

# Rota para predições
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obter os dados enviados no corpo da requisição
        data = request.json

        # Pré-processar os dados
        features = preprocess_input(data)

        # Fazer a predição
        prediction = model.predict(features)
        prediction_proba = model.predict_proba(features)

        # Converter a predição para a categoria original
        prediction_categorical = resultado_encoder.inverse_transform(prediction)

        # Log de saída
        print(f"Predição numérica: {prediction[0]}, Probabilidades: {prediction_proba[0]}")

        # Retornar os resultados
        return jsonify({
            "inputs": data,
            "prediction": prediction_categorical[0],  # Categoria original
            "prediction_proba": prediction_proba.tolist()
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
