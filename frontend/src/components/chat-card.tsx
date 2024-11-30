import React from 'react';
import { useNavigate } from 'react-router-dom';

interface IChatCardProps {
  chatName: string;
  description: string;
  imageUrl: string;
}

export const ChatCard: React.FC<IChatCardProps> = ({ chatName, description, imageUrl }) => {
  const navigate = useNavigate();
  return (
    <div onClick={() => navigate('/chats-members')} className="chat-card">
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
