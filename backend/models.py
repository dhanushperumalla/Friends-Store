from app import db

class Friend(db.Model):
    __tablename__ = 'friends'  # Optionally specify the table name

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Fixed typo: nullabe -> nullable
    role = db.Column(db.String(50), nullable=False)   # Fixed typo: nullabe -> nullable
    description = db.Column(db.Text, nullable=False)  # Fixed typo: nullabe -> nullable
    gender = db.Column(db.String(10), nullable=False) # Fixed typo: nullabe -> nullable
    img_url = db.Column(db.String(200), nullable=True) # Fixed typo: nullabe -> nullable
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "description": self.description,
            "gender": self.gender,
            "imgUrl": self.img_url
        }
