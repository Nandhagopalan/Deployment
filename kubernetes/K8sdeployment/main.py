import os
from transformers import pipeline
from flask import Flask
import json
from flask import Flask, request, jsonify


ner_pipe = pipeline("ner",model="dslim/bert-base-NER",device=0)


app = Flask(__name__)


@app.route("/ner", methods=["POST"])
def hello_k8s():
    sequence = request.json["input"]
    results=ner_pipe(sequence)

    out=[]
    start=None
    end=None
    ent=None
    for result in results:

        if start is None:        
            if result['entity'].startswith('B-'):
                start=result['start']
                end=result['end']
                ent=result['entity']

        elif start is not None and result['entity'].split('-')[-1]==ent.split('-')[-1] and result['entity'].startswith('I-'):
                end=result['end']

        elif start is not None and result['entity'].startswith('B-'):
                out.append({'word':sequence[start:end],'ent':ent.split('-')[-1]})
                start=result['start']
                end=result['end']
                ent=result['entity']

    if start is not None:     
        out.append({'word':sequence[start:end],'ent':ent.split('-')[-1]})
        
    return json.dumps(out)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)