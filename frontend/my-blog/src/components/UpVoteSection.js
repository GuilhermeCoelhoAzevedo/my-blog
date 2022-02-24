const UpVoteSection = ( {articleName, upVotes, setArticleinfo} ) => {
    const upVoteArticle = async () => {
        await fetch(`/api/articleUpVote/${articleName}`, {
            method: 'post',
        })
        .then(res => res.json())
        .then(json => setArticleinfo(json));
    };

    return (
        <div id="upvotes-section"> 
            <button onClick={() => upVoteArticle()}>Add Upvote</button>
            <p>This post has been upvoted {upVotes} times</p>
        </div>
    );
};

export default UpVoteSection;