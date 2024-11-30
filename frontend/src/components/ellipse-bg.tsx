import React from 'react';
import '../sass/ellipse-bg.scss';

const EllipsesBackground: React.FC = () => {
    return (
        <div className="ellipses-background">
            <div className="ellipse ellipses-background__left" />
            <div className="ellipse ellipses-background__right" />
            <div className="ellipse__top ellipses-background__top" />
            <div className="ellipse__top ellipses-background__bottom" />
        </div>
    );
};

export default EllipsesBackground;