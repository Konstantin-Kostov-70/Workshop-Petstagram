def get_all_liked_photos_by_request_user(request):
    all_liked_photos_by_request_user = []
    user = request.user
    if user.is_authenticated:
        all_liked_photos_by_request_user = [like.to_photo_id for like in user.like_set.all()]
        return all_liked_photos_by_request_user
    return all_liked_photos_by_request_user
