def test_read_prayers_empty(client):
    """Test GET /api/v1/prayers/ with empty database."""
    response = client.get("/api/v1/prayers/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_prayer(client):
    """Test POST /api/v1/prayers/."""
    prayer_data = {
        "title": "Our Father",
        "text": "Our Father who art in heaven...",
        "category": "Basic",
    }
    response = client.post("/api/v1/prayers/", json=prayer_data)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Our Father"
    assert "id" in data
    assert data["category"] == "Basic"


def test_read_prayers_after_create(client):
    """Test GET /api/v1/prayers/ after creating an item."""
    # Primeiro cria uma oração
    prayer_data = {
        "title": "Hail Mary",
        "text": "Hail Mary, full of grace...",
        "category": "Mary",
    }
    create_response = client.post("/api/v1/prayers/", json=prayer_data)
    created_id = create_response.json()["id"]

    # Depois verifica a lista
    response = client.get("/api/v1/prayers/")
    assert response.status_code == 200
    data = response.json()

    # Verifica se a oração criada está na lista
    assert len(data) == 1
    assert data[0]["title"] == "Hail Mary"
    assert data[0]["id"] == created_id
