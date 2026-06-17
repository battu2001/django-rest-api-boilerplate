from django.core.cache import cache

def get_cached_user(user_id: int):
    """Get user from cache or DB with Redis."""
    cache_key = f"user:{user_id}"
    user = cache.get(cache_key)
    if not user:
        from apps.users.models import User
        try:
            user = User.objects.select_related().get(id=user_id)
            cache.set(cache_key, user, timeout=300)
        except User.DoesNotExist:
            return None
    return user

def invalidate_user_cache(user_id: int):
    """Invalidate user cache on update."""
    cache.delete(f"user:{user_id}")
