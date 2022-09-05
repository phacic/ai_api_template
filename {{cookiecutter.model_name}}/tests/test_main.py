import pytest
from fastapi import status


@pytest.mark.asyncio
async def test_root(app_client):
    resp = app_client.get("/")

    # should be redirect response with status 307
    assert resp.history[0].status_code == status.HTTP_307_TEMPORARY_REDIRECT

    # actual response should be 200
    assert resp.status_code == status.HTTP_200_OK

    # url after redirect should be /docs
    assert resp.request.path_url == "/docs"
