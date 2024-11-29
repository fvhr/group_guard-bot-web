import React from 'react';
import '../sass/chatCard.scss';

interface IChatCardProps {
    chatName: string;
    description: string;
    imageUrl: string;
}

const ChatCard: React.FC<IChatCardProps> = ({ chatName, description, imageUrl }) => {
    return (
        <div className="chat-card">
            <div className="chat-card__image">
                <img src={imageUrl} alt={chatName} />
            </div>
            <div className="chat-card__content">
                <p className="chat-card__chat-name">{chatName}</p>
                <p className="chat-card__description">{description}</p>
            </div>
        </div>
    );
};

export default ChatCard;