import React, { useState, useEffect } from 'react'
import { useParams } from "react-router-dom";
import articleContent from './article-content';
import ArticlesList from '../components/ArticlesList';
import CommentsList from '../components/CommentsList';
import UpVoteSection from '../components/UpVoteSection';
import AddCommentForm from '../components/AddCommentForm';
import NotFoundPage from './NotFoundPage'

const ArticlePage = () => {
    const { name }  = useParams();
    const article = articleContent.find(article => article.name===name);
    const otherArticles = articleContent.filter(article => article.name !== name);
    const [articleInfo, setArticleInfo] = useState({ upVotes: 0, comments: []});
    
    useEffect(() => {
        const fetchData = async () => {
            const result = await fetch(`/api/article/${name}`);
            const body = await result.json();
            setArticleInfo(body);        
        }
        fetchData();
    }, [name]);
    
    if (!article) return <NotFoundPage />

    return(
        <>
        <h1>{article.title}</h1>
        <UpVoteSection articleName={name} upVotes={articleInfo.upVotes} setArticleinfo={setArticleInfo}/>
        {article.content.map((paragraph, key) => (
            <p key={key}>{paragraph}</p>
        ))}
        <AddCommentForm  articleName={name} setArticleinfo={setArticleInfo} />
        <CommentsList comments={articleInfo.comments}/>
        <h3>Other articles:</h3>
        <ArticlesList articles={otherArticles} />
        </>
    )
}

export default ArticlePage;