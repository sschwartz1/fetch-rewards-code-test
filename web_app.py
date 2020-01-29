from similarity_scorer import SimilarityScorer
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/score_similarity", methods= ['POST'])
def process_score():
    # Assumed body was json object with 2 texts, keys are 'text1' and 'text2'
    data = request.get_json()
    if len(data) == 2:
        try:
            scorer = SimilarityScorer(data['text1'], data['text2'])
            scorer.create_count_dict()
            final_score = scorer.compare_texts()
            response = {'status' : 'ok'}
        except:
            response = {
                'status' : 'error',
                'message' : 'Payload must be keys "text1" and "text2" containing a string in each'
            }
    else:
        response = {
            'status' : 'error', 
            'messgae' : 'Incorrect number of text arguements'
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run()