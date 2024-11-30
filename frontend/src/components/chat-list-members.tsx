import { Alert } from '@mui/material';
import { CheckIcon } from 'lucide-react';
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { ChatType } from '../types/chat';
import { User } from '../types/members';
import { MenuMembers } from './menu-members';

type Props = {
  members: User[];
  error: Error | null;
  chatInfo: ChatType | undefined;
  loaders: JSX.Element[];
  isLoading: boolean;
};

export const ChatListMembers: React.FC<Props> = ({
  chatInfo,
  members,
  isLoading,
  error,
  loaders,
}) => {
  const [isMenuOpen, setIsMenuOpen] = useState<number | null>(null);
  const [alertMessage, setAlertMessage] = useState<string | null>(null);

  const navigate = useNavigate();

  const toggleMenu = (id: number) => {
    setIsMenuOpen(isMenuOpen === id ? null : id);
  };

  const handleRemoveFromChat = () => {
    setAlertMessage('Удален из чата');
    setIsMenuOpen(null);

    setTimeout(() => {
      setAlertMessage(null);
    }, 2000);
  };

  const handleRemoveFromAllChats = () => {
    setAlertMessage('Удален из чатов');
    setIsMenuOpen(null);

    setTimeout(() => {
      setAlertMessage(null);
    }, 2000);
  };

  const handleCloseAlert = () => {
    setAlertMessage(null);
  };

  return (
    <>
      {alertMessage && (
        <Alert
          icon={<CheckIcon fontSize="inherit" style={{ color: 'green' }} />}
          severity="success"
          onClose={handleCloseAlert}
          style={{
            position: 'absolute',
            bottom: '80px',
            left: '50%',
            transform: 'translateX(-50%)',
            zIndex: 1000,
            border: '1px solid green',
            color: 'green',
          }}>
          {alertMessage}
        </Alert>
      )}
      <div className="chat-list-members__header">
        <div onClick={() => navigate('/chats')} className="chat-list-members__back">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="32"
            height="32"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            className="lucide lucide-undo-2">
            <path d="M9 14 4 9l5-5" />
            <path d="M4 9h10.5a5.5 5.5 0 0 1 5.5 5.5a5.5 5.5 0 0 1-5.5 5.5H11" />
          </svg>
          <div className="chat-list-members__back-text">Назад</div>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
          <img src={chatInfo?.avatar_url} alt="Chat" />
          <div className="chat-list-members__chat-image">
            <div>{chatInfo?.title}</div>
            <span>{members.length} участников</span>
          </div>
        </div>
      </div>
      {isLoading && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '20px', width: '600px' }}>
          {loaders}
        </div>
      )}
      {error && <p>Error: {error.message}</p>}

      <div className="chat-list-members__list">
        {members.map((member) => (
          <div
            onClick={() => toggleMenu(member.id)}
            className="chat-list-members__item"
            key={member.id}>
            <div style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
              <div className="chat-list-members__avatar">
                <img src={member.photo_url} alt={member.username} />
              </div>
              <div className="chat-list-members__data">
                <div className="chat-list-members__name">{member.first_name}</div>
                <span className="chat-list-members__username">{member.username}</span>
              </div>
            </div>

            <div className="chat-list-members__role">владелец</div>
            {isMenuOpen === member.id && (
              <MenuMembers
                handleRemoveFromChat={handleRemoveFromChat}
                handleRemoveFromAllChats={handleRemoveFromAllChats}
              />
            )}
          </div>
        ))}
      </div>
    </>
  );
};
