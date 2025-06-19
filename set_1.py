def savings(gross_pay, tax_rate, expenses):
    take_home = int(gross_pay * (1 - tax_rate)) 
    return take_home - expenses

def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_consumed = num_jobs * job_consumption
    remaining = total_material - total_consumed
    return str(remaining) + material_units

def interest(principal, rate, periods):
    final_value = principal + int(principal * rate * periods)
    return final_value

