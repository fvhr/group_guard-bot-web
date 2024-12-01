import React from 'react';
import { useNavigate } from 'react-router-dom';

interface IChatCardProps {
  id: number;
  chatName: string;
  description: string;
  imageUrl: string;
}

export const ChatCard: React.FC<IChatCardProps> = ({ id, chatName, description, imageUrl }) => {
  const navigate = useNavigate();
  return (
    <div onClick={() => navigate(`/chats-member/${id}`)} className="chat-card">
      <div className="chat-card__image">
        {imageUrl.startsWith('f') ? (
          <div className="chat-card__default">
            <span>{chatName.charAt(0)}</span>
          </div>
        ) : (
          <img src={imageUrl} alt={chatName} />
        )}
      </div>
      <div className="chat-card__content">
        <p className="chat-card__chat-name">{chatName}</p>
        <p className="chat-card__description">
          {description === null ? 'Нет описания' : description}
        </p>
      </div>
    </div>
  );
};
