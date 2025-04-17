def calculated_salary(hourly_rate, hours_worked, tax_rate=0.15):
    gross_salary = hourly_rate * hours_worked

    tax = gross_salary * tax_rate
    net_salary = gross_salary * tax

    return net_salary


