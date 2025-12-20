score = 85

if score >= 90:
    grade = "5"
elif score >= 75:
    grade = "4"
elif score >= 60:
    grade = "3"
else:
    grade = "2"

print(f"Оценка: {grade}")


status = "отлично" if score > 80 else "нужно улучшить"
print(status)