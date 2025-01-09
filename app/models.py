from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash , check_password_hash

db = SQLAlchemy()

class User( UserMixin ,db.Model):
    id = db.Column(db.Interger, primary_key = True)
    username = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    password_hash = db.Column(db.String(100), nullable = False)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    phone = db.Column(db.String(20), nullable = False)
    address = db.Column(db.Text)
    role = db.Column(db.String(20), default = "customer")
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Food(db.Model):
    id = db.Column(db.Interger, primary_key = True)
    name = db.Column(db.String(100) , nullable= False)
    descirption = db.Column(db.Text)
    price = db.Column(db.Float , nullale = False)
    category_id = db.Column(db.String(100), nullable = False)
    image_url = db.Column(db.Interger , db.Foreign_key("category_id") , nullable = False)
    
    category = db.relationship("Category", backref=db.backref("dishes", lazy=True))
    reviews = db.relationship("Review" , backref = "food" , lazy = True)
class Category(db.Model):
    id = db.Column(db.Interger, primary_key = True)
    name = db.Column(db.String(255), unique =True, nullable = False)
    
    dishes = db.relationship("Food" , backref = "category" , lazy = True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    total_price = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(50), default='pending')  # Trạng thái: pending, completed, canceled
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

#Chi tiết đơn hàng
class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    order = db.relationship('Order', backref=db.backref('order_items', lazy=True))
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'))
    dish = db.relationship('Dish')
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    total = db.Column(db.Numeric(10, 2), nullable=False)

#Đánh giá người dùng 
class Review(db.Model):
    id = db.Column(db.Interger , primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Người dùng viết review
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'), nullable=False)  # Món ăn được đánh giá
    rating = db.Column(db.Integer, nullable=False)  # Đánh giá món ăn (thường từ 1 đến 5)
    content = db.Column(db.Text)  # Nội dung đánh giá
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Mối quan hệ với User (review được viết bởi người dùng)
    user = db.relationship('User', backref=db.backref('reviews', lazy=True))
    
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))  # Liên kết với đơn hàng
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)  # Tổng tiền thanh toán
    payment_method = db.Column(db.String(50))  # Phương thức thanh toán (ví dụ: credit card, cash, online)
    payment_status = db.Column(db.String(50), default='unpaid')  # Trạng thái thanh toán: unpaid, paid
    paid_amount = db.Column(db.Numeric(10, 2), default=0)  # Số tiền đã thanh toán
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    # Tham chiếu tới bảng Order
    order = db.relationship('Order', backref=db.backref('payment', uselist=False))