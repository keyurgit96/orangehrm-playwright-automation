class Endpoints:

    API_V2 = "/web/index.php/api/v2"

    # Authentication
    AUTH_LOGIN = "/auth/login"

    # Recruitment
    RECRUITMENT_CANDIDATES = f"{API_V2}/recruitment/candidates"

    @staticmethod
    def candidate_by_id(candidate_id: int | str) -> str:
        return f"{Endpoints.RECRUITMENT_CANDIDATES}/{candidate_id}"

    # Attendance & Timesheet
    ATTENDANCE_RECORDS = f"{API_V2}/attendance/records"
    ATTENDANCE_RECORDS_LATEST = f"{API_V2}/attendance/records/latest"

    # Employee / User Information
    @staticmethod
    def employee_name(employee_id: int | str) -> str:
        return f"{Endpoints.API_V2}/admin/employees/{employee_id}/name"

    @staticmethod
    def employee_personal_details(employee_id: int | str) -> str:
        return f"{Endpoints.API_V2}/pim/employees/{employee_id}/personal-details"
