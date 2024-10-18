from datetime import datetime, timezone

today = datetime.now(timezone.utc)
# Unix epoch
epoch = datetime.fromtimestamp(0, timezone.utc)

# Delta between today and Unix epoch
delta = today - epoch
delta_seconds = delta.total_seconds()

# Formating
formated_today = today.strftime("%b %-d %Y")
formated_epoch = epoch.strftime("%B %-d, %Y")
formated_seconds = f"{delta_seconds:,.4f}"
scientific_notation = "{:.2e}".format(delta_seconds)

print(f"Seconds since {formated_epoch}: {formated_seconds} or {scientific_notation} in scientific notation")
print(formated_today)
