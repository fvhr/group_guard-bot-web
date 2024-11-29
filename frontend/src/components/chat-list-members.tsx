import React, { useState } from 'react';


interface IMember {
  id: number;
  name: string;
  avatarUrl: string;
}

interface IChatListMembersProps {
  chatName: string;
  chatMembersCount: number;
  chatImageUrl: string;
  members: IMember[];
}

export const ChatListMembers: React.FC<IChatListMembersProps> = ({
  chatName,
  chatMembersCount,
  chatImageUrl,
  members,
}) => {
  const [isMenuOpen, setIsMenuOpen] = useState<number | null>(null);

  const toggleMenu = (id: number) => {
    setIsMenuOpen(isMenuOpen === id ? null : id);
  };

  const handleRemoveFromChat = (id: number) => {
    alert(`Кикнут участник ${id} из этого чата.`);
  };

  const handleRemoveFromAllChats = (id: number) => {
    alert(`Кикнут участник ${id} из всех чатов.`);
  };

  return (
    <>
      <div className="chat-list-members__header">
        <div className="chat-list-members__chat-image">
          <img src={chatImageUrl} alt="Chat" />
          <h1>{chatName}</h1>
        </div>
        <h2>{chatMembersCount} участников</h2>
      </div>

      <div className="chat-list-members__list">
        {members.map((member) => (
          <div className="chat-list-members__item" key={member.id}>
            <div className="chat-list-members__avatar">
              <img src={member.avatarUrl} alt={member.name} />
            </div>
            <div className="chat-list-members__name">{member.name}</div>

            <div className="chat-list-members__menu">
              <button
                className="chat-list-members__menu-button"
                onClick={() => toggleMenu(member.id)}>
                ⋮
              </button>
              {isMenuOpen === member.id && (
                <div className="chat-list-members__dropdown">
                  <button onClick={() => handleRemoveFromChat(member.id)}>
                    Удалить из этого чата
                  </button>
                  <button onClick={() => handleRemoveFromAllChats(member.id)}>
                    Удалить из всех чатов
                  </button>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
    </>
  );
};
