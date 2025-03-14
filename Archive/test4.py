from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get('/multiplication')
def multiplication(
    length: int,
    width: int,
    depth: Optional[int] = None
) -> int:
    res = length * width
    if depth is not None:
        res = res * depth
    return res
