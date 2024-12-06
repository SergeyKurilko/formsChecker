from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from database import get_templates, Template
from validators import validate_field

app = FastAPI()

@app.post("/get_form")
async def get_form(request: Request):
    # Извлекаем данные из x-www-form-urlencoded запроса
    form_data = await request.form()

    # Создаем dict_items из FormData
    form_fields = {key: value for key, value in form_data.items()}

    # Шаблоны из БД
    templates = get_templates()

    matched_template = None

    for template in templates:
        template_fields = {key: value for key, value in template.items() if key != "name"}

        # Ищем совпадения пришедшей формы с шаблонами и валидируем
        if all(field in form_fields and validate_field(
                form_fields[field]) == template_fields[field]
               for field in template_fields):
            matched_template = template["name"]
            break

    # Если все поля совпали и прошли валидацию, то возвращаем name формы
    if matched_template:
        return JSONResponse(content={"form_name": matched_template})
    # Если шаблон не найден, то сравниваем поля из полученной формы с шаблонами.
    # Возвращаем поля и типы, если нашли.
    else:
        field_types = {}
        for key, value in form_fields.items():
            for template in templates:
                if key in template:
                    field_types[key] = template[key]

        return JSONResponse(content=field_types)