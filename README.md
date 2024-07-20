# InstagramPy

Esta biblioteca foi criada para fins educacionais e fornece funcionalidades para interagir com Instagram

## Aviso Legal
**Aviso: Esta biblioteca não é afiliada ou endossada por Instagram. Use por sua conta e risco. Esta biblioteca foi criada apenas para fins educacionais e não deve ser usada em produção. O uso desta biblioteca pode violar os Termos de Serviço de Instagram**

## Uso
```python
from InstagramPy import *

#Criar um arquivo contendo cookies e headers
client = InstagramPy("user")
```



Puxar informações do perfil 
```python
client.profile("username")
```

Puxar lista de seguidores 
```python
client.get_follower(id_user, count)
```

Puxar status da lista de seguidores 
exemplo: Se ja esta seguindo, perfil privado etc
```python
client.show_many(user_ids)
```

Puxar lista de seguidores + status 
```python
client.get_followerV2(user_id)
```

Seguir usuário 
```python
client.follower(user_id)
```

Deixar de seguir usuário 
```python
client.unfollower(user_id)
```
