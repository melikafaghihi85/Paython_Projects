def divide(a, b):
    return a / b

while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        result = divide(num1, num2)
        print("Result:", result)
        break  

    except ValueError:
        print("خطا: لطفاً فقط عدد صحیح وارد کنید.")

    except ZeroDivisionError:
        print("خطا: تقسیم بر صفر مجاز نیست. لطفاً عدد دوم را غیر از صفر وارد کنید.")

    finally:
        print("!برنامه با موفقیت اجرا شد")3