
from plyer import notification as noti

noti.notify(
    title="Medication Alert",
    message="It's 9:00. Time to take your meds.\n"
            "x3 Zonisimide\n"
            "x1 Keppra\n"
            "x1 Lamictal\n"
            "x1 Spironolactone",
    app_icon="favicon_package_v0.16/favicon.ico",
    timeout=50
)


