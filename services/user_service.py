from sqlalchemy import or_
from extensions import db
from models.user_model import User

def get_users(search=None, page=1, limit=10):
    query = User.query

    if search:
        search_text = f"%{search}%"
        query = query.filter(
            or_(
                User.name.like(search_text),
                User.email.like(search_text)
            )
        )

    paginated_users = query.order_by(User.id.desc()).paginate(
        page=page,
        per_page=limit,
        error_out=False
    )

    return {
        "users": [user.to_dict() for user in paginated_users.items],
        "total": paginated_users.total,
        "page": page,
        "limit": limit,
        "pages": paginated_users.pages
    }


def create_user(data):
    existing_user = User.query.filter_by(email=data["email"]).first()

    if existing_user:
        return None, "Email already exists"

    user = User(
        name=data["name"],
        email=data["email"],
        role=data["role"]
    )

    db.session.add(user)
    db.session.commit()

    return user.to_dict(), None


def get_user_by_id(user_id):
    user = User.query.get(user_id)

    if not user:
        return None

    return user.to_dict()