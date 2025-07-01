from flask import Flask, request, jsonify
from dateutil import parser
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    params = req['queryResult']['parameters']
    print(" Dữ liệu nhận được từ Dialogflow:", params)

    person = params.get('person', {}).get('name', 'bạn')
    dichvu = params.get('dichvu')
    date = params.get('date')
    time = params.get('time')
    LoaiKham = params.get('Loaikham')
    phone = params.get('phone')
    email = params.get('email')

    date_formatted = parser.parse(date).strftime('%d/%m/%Y')
    time_formatted = parser.parse(time).strftime('%H:%M')

    reply = f"Bạn {person} đã đặt lịch khám {LoaiKham} lúc {time_formatted} ngày {date_formatted}. Chúng tôi sẽ liên hệ qua số {phone} và {email}."
    return jsonify({"fulfillmentText": reply})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
