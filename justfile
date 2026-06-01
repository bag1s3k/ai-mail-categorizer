set shell := ["powershell"]

uv_cmd := "uv run"

run:
    @{{uv_cmd}} -m ai_mail_categorizer

ruff path="":
    @{{uv_cmd}} ruff check --fix {{path}}
    @{{uv_cmd}} ruff format {{path}}

format path="":
    @{{uv_cmd}} ruff format {{path}}

check path="" fix="":
    @{{uv_cmd}} ruff check {{fix}} {{path}}

watch:
    @{{uv_cmd}} ruff check --watch