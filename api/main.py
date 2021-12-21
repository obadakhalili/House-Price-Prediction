import os
from functools import reduce
from flask import Flask, request
import pandas as pd


def main():
    pickles_dir = os.path.join(os.path.dirname(__file__), '../ML/pickles')
    model = pd.read_pickle(f"{pickles_dir}/model.pickle")
    considered_features_order = pd.read_pickle(
        f"{pickles_dir}/considered_features_order.pickle")

    app = Flask("House Price Prediction")

    app.config['JSON_SORT_KEYS'] = False

    @app.route("/predict", methods=["POST"])
    def predict():
        try:
            model_input = reduce(
                lambda model_input, feature: {
                    **model_input, feature: request.json[feature]
                }, considered_features_order, {})

            return {"prediction": model.predict([model_input])[0]}
        except KeyError as not_found_feature:
            return f"Didn't find feature: {not_found_feature}", 400
        except Exception:
            return "Internal server error", 500

    port = os.environ.get("PORT", 8081)
    app.run(port=port, host="0.0.0.0")


if __name__ == "__main__":
    main()
