def friends_list (user, *friends):
    """Prints a list of friends."""
    print(f"{user.title()}'s friends are:")
    for friend in friends:
        print(f"- {friend.title()}")

friends_list('faasen','alice', 'bob', 'charlie')
friends_list('mike','david', 'eva')

