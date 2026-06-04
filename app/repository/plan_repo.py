from app import db
from app.model.plan import Plan

class PlanRepository:

    @staticmethod
    def save(plan: Plan) -> Plan:
        db.session.add(plan)
        db.session.commit()

        return plan

    @staticmethod
    def find_by_user_id(
            user_id: int,
            page: int,
            page_size: int
    ):
        return (
            Plan.query
            .filter_by(user_id=user_id)
            .order_by(Plan.create_time.desc())
            .paginate(
                page=page,
                per_page=page_size,
                error_out=False
            )
        )