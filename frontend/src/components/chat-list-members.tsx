import { Alert } from '@mui/material';
import { CheckIcon } from 'lucide-react';
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { IChatListMembersProps } from '../types/members';
import { MenuMembers } from './menu-members';

export const ChatListMembers: React.FC<IChatListMembersProps> = ({
  chatName,
  chatMembersCount,
  chatImageUrl,
  members,
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
          icon={<CheckIcon fontSize="inherit" style={{ color: 'white' }} />}
          severity="success"
          onClose={handleCloseAlert}
          style={{
            position: 'absolute',
            bottom: '80px',
            left: '50%',
            transform: 'translateX(-50%)',
            zIndex: 1000,
            background: '#414d5a',
            color: 'white',
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
          Назад
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
          <img src={chatImageUrl} alt="Chat" />
          <div className="chat-list-members__chat-image">
            <div>{chatName}</div>
            <span>{chatMembersCount} участников</span>
          </div>
        </div>
      </div>

      <div className="chat-list-members__list">
        {members.map((member) => (
          <div
            onClick={() => toggleMenu(member.id)}
            className="chat-list-members__item"
            key={member.id}>
            <div style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
              <div className="chat-list-members__avatar">
                <img src={member.avatarUrl} alt={member.name} />
              </div>
              <div className="chat-list-members__name">{member.name}</div>
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
