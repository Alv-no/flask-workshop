from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from models import EventModel
from schemas import EventSchema
from db import db

blp = Blueprint("events", __name__, description="Operations on events")

@blp.route("/event/<int:id>")
class Event(MethodView):
    
    @blp.response(200, EventSchema)
    def get(self, id):
        event = EventModel.query.get_or_404(id)
        return event

@blp.route("/event")   
class EventList(MethodView):
    
    @blp.arguments(EventSchema)
    @blp.response(200, EventSchema)
    def post(self, event_data):
        event = EventModel(**event_data)
        
        try:
            db.session.add(event)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Could not insert an event.")
        
        return event
        
        
        
        
        
        
        
        





