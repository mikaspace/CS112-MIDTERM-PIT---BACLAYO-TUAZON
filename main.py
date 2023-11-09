# Dictionary to store user credentials (in-memory storage)
user_accounts = {}
# Dictionary to store blog posts
blog_posts = {}

# Function for user registration (Sign Up)
def register_user(username, password):
    if username in user_accounts:
        print("Username already exists. Please choose a different one.")
    else:
        user_accounts[username] = password
        print("Account created successfully. You can now log in.")

# Function for user login (Sign In)
def login_user(username, password):
    if username in user_accounts and user_accounts[username] == password:
        print(f"Welcome, {username}!")
        return username
    else:
        print("Invalid username or password. Please try again.")
        return None

# Function for posting a blog
def post_blog(username, title, content):
    if username:
        blog_posts[title] = content
        print(f"Blog post '{title}' added successfully!")
    else:
        print("You need to log in to post a blog.")

# Function for viewing blogs
def view_blogs():
    if blog_posts:
        print("\n--- Blog Posts ---")
        for title, content in blog_posts.items():
            print(f"Title: {title}\nContent: {content}\n")
    else:
        print("No blog posts available.")

print

print("-------Welcome to Nyka!-------\nWhere you can express yourself\n    within your own space.\n------------------------------\n")
print("~~ Nyka, your safe space ~~\n")

# Main program loop
logged_in_user = None
while True:
    print("1. Sign Up")
    print("2. Sign In")
    print("3. Post a Blog")
    print("4. View Blogs")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        new_username = input("Enter a username: ")
        new_password = input("Enter a password: ")
        register_user(new_username, new_password)
    elif choice == '2':
        log_username = input("Enter your username: ")
        log_password = input("Enter your password: ")
        logged_in_user = login_user(log_username, log_password)
    elif choice == '3':
        if logged_in_user:
            blog_title = input("Enter blog title: ")
            blog_content = input("Enter blog content: ")
            post_blog(logged_in_user, blog_title, blog_content)
        else:
            print("You need to log in to post a blog.")
    elif choice == '4':
        view_blogs()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, 4, or 5.")