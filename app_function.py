import sqlite3


def get_db_conn():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def save_post(title, content):
    # 这里应该是将标题和内容保存到数据库的代码。例如：
    conn = get_db_conn()
    conn.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()


def delete_post(post_id):
    conn = get_db_conn()
    conn.execute("DELETE FROM posts WHERE id=?", (post_id,))
    conn.commit()
    conn.close()


def get_post(post_id):
    conn = get_db_conn()
    post = conn.execute('select * from posts where id = ?', (post_id, )).fetchone()
    return post


def edit_post(title, content, post_id):
    conn = get_db_conn()
    conn.execute("UPDATE posts SET title =?, content=? WHERE id=?",
                 (title, content, post_id))
    conn.commit()
    conn.close()
