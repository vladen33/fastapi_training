from fastapi import FastAPI, Query

app = FastAPI()

@app.get('/math-sum')
def math_sum(
    add: list[float] = Query(gt=0, lt=9.99, title='Суммирование дробных чисел',
                             description='Суммирует дробные числа и отдает результат')
) -> float:
    return round(sum(add), 2)