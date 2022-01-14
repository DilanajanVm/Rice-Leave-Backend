from dataclasses import dataclass

from flask import Flask, request, jsonify, make_response, render_template, url_for
from flask.sessions import NullSession
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy


application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ricecrop:123456Dila@aa4lngkmgkzx6b.clrek8hccwfs.us-east-1.rds.amazonaws.com:3306/ebdb'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['CORS_HEADERS'] = 'Content-Type'
application.secret_key = "secret key"
application.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
cors = CORS(application)
db = SQLAlchemy(application)

@dataclass()
class User(db.Model):
    id:int
    imgName : str
    desc : str

    id = db.Column(db.Integer, primary_key=True)
    imgName = db.Column(db.String(200), unique=False, nullable=False)
    desc = db.Column(db.String(400), unique=False, nullable=False)

    def __init__(self,id,imgName,desc) -> None:
        self.id = id
        self.imgName=imgName
        self.desc=desc


db.create_all()
db.session.commit()

@application.route('/')
def home():
    return jsonify({ 'status':'success' })


@application.route("/dashboard", methods=['GET'])
@cross_origin()
def dashboard():
    try:
        result = request.args.get('filename')

        imgName=''
        status=''
        desc = ''

        if result == '1.png':
             imgName = result
             status = 'Healthy'
             desc = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. '
             solution = 'Rice crops are Healthy'
        elif result == '2.png':
             imgName = result
             status = 'Brown Spots'
             desc = 'Brown spot of rice is a plant fungal disease that usually occurs on the host leaves and glume, as well as seedlings, sheaths, stems and grains of adult host plants. Hosts include Oryza (Asian rice), Leersia (Cutgrass), Zizania (Wild rice), and other species as well such as Echinochloa colona (junglerice) and Zea mays (maize).Cochliobolus miyabeanus may cause a wide range of symptoms. General symptoms occurring on the hosts can be observed on many parts of the plant, including leaves, seeds, stems and inflorescences, along with the presence of brown spot. Discoloration of stems is another symptom develops from brown spot of rice disease. Oval-shaped brown spots are the fungal growth sign, which have grey colored center developed on host leaves.Dark coffee-coloured spots appear in the panicle and severe attacks cause spots in the grain and loss of yield and milling quality.'
             solution = 'The spread of the fungus can be prevented by using certified disease-free seed and using available resistant varieties such as MAC 18. \n Avoiding dense sowing will can also help prevent the spread of the fungus as it reduces humidity \n Maintaining control of weeds and removal of volunteer crops in the field can also prevent fungal spread,as well as burning the stubble of infected plants. \n Seed treatments can also be used as a preventative measure. Seeds can be treated with fungicides or alternatively soaking seeds in cold water for 8 hours before treating with hot water (53-54°C) for 10-12 minutes prior to planting. \n Soil treatments can also be used to prevent the spread of C. miyabeanus. The addition of potassium and calcium if the soil is deficient can help boost disease resistance. \n However, excessive application of nitrogen fertilisers should be avoided.'
        elif result == '3.png':
             imgName = result
             status = 'Hispa'
             desc = 'What is the meaning of rice hispa? \n Rice Hispa (pamripoka) an insect pest, Dicladispa armigera, of the family Hispidae, order Coleoptera. ... Since then its occurrence as a major pest and sporadic, wide-spread outbreaks have been reported from many districts of Bangladesh.',
             solution = 'Avoid over fertilizing the field \nClose plant spacing results in greater leaf densities that can tolerate higher hispa numbers. \n Leaf tip containing blotch mines should be destroyed.\nManual collection and killing of beetles – hand nets. \n Clipping and burying shoots in the mud can reduce grub populations by 75 - 92%.'
        elif result == '4.png':
             imgName = result
             status = 'Leaf Blast'
             desc = 'What is the meaning of rice hispa? \n Rice Hispa (pamripoka) an insect pest, Dicladispa armigera, of the family Hispidae, order Coleoptera. ... Since then its occurrence as a major pest and sporadic, wide-spread outbreaks have been reported from many districts of Bangladesh.',
             solution = 'Avoid over fertilizing the field \nClose plant spacing results in greater leaf densities that can tolerate higher hispa numbers. \n Leaf tip containing blotch mines should be destroyed.\nManual collection and killing of beetles – hand nets. \n Clipping and burying shoots in the mud can reduce grub populations by 75 - 92%.'
        else:
            imgName = result
            status = 'Fruit Fly '
            desc = 'What is the meaning of rice hispa? \n Rice Hispa (pamripoka) an insect pest, Dicladispa armigera, of the family Hispidae, order Coleoptera. ... Since then its occurrence as a major pest and sporadic, wide-spread outbreaks have been reported from many districts of Bangladesh.',
            solution = 'Avoid over fertilizing the field \nClose plant spacing results in greater leaf densities that can tolerate higher hispa numbers. \n Leaf tip containing blotch mines should be destroyed.\nManual collection and killing of beetles – hand nets. \n Clipping and burying shoots in the mud can reduce grub populations by 75 - 92%.'
           
        return make_response(jsonify({
            "success": "true",
            "data": {
                "imageName": result,
                "status": status,
                "desc": desc,
                "solution":solution
            },
            "status": "200"
        }), 200)
    except:
        return 'test again'


@application.route("/sendImageDetails", methods=['POST'])
@cross_origin
def sendImageDetails():
    result = 'post'
    # data = request.form['imageNmae']
    # if request.method == 'POST':
    #     Imagename =  data.get('imageNmae')
    #     print(Imagename)

    return make_response(jsonify({
            "success": "true",
            "data": {
                "noOfVehicles": 'result'
            },
            "status": "200"
        }), 200)


if __name__ == '__main__':
    application.run(debug=True)