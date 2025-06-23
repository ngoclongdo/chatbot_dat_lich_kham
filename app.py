from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    params = req['queryResult']['parameters']

    name = params.get('Name', 'bạn')
    dichvu = params.get('dichvu')
    date = params.get('date')
    time = params.get('time')
    LoaiKham = params.get('Loaikham')
    phone = params.get('phone')
    email = params.get('email')


    reply = f"✅ Bạn {name} đã đặt lịch {dichvu} {LoaiKham} lúc {time} ngày {date}. Chúng tôi sẽ liên hệ qua số {phone} và {email}."
    return jsonify({"fulfillmentText": reply})

if __name__ == '__main__':
    app.run(port=5000)
