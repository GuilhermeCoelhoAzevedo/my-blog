import { useState } from 'react';

const AddCommentForm = ( { articleName, setArticleinfo} ) => {
    const[username, setUsername] = useState('');
    const[commentText, setCommentText] = useState('');

    const addComment = async () => {
        await fetch(`/api/addComment/${articleName}`, {
            method: 'post',
            body: JSON.stringify({ username, text: commentText }),
            headers : {
                'Content-Type' : 'application/json',
            }
        })
        .then(res => res.json())
        .then(json => setArticleinfo(json));
        
        setUsername('');
        setCommentText('');
    };
    
    return (
        <div id="add-comment-form">
            <h3>Add a Comment</h3>
            <label>
                Name:
                <input type="text" value={username} onChange={(event) => setUsername(event.target.value)}/>
            </label>
            <label>
                Comment:
                <textarea rows="4" cols="50" value={commentText} onChange={(event) => setCommentText(event.target.value)}/>
            </label>
            <button onClick={() => addComment()}>Add Comment</button>
        </div>
    );
};

export default AddCommentForm;