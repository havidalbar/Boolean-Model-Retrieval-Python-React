import React,{useState} from 'react';
import { Skeleton, Switch, Card, Avatar } from 'antd';
const { Meta } = Card;



export default function CardPenyakit(props){
   let {img, content, title} = props.value;
    return(
        <Card style={{ width: 1000 }} >
          <Meta
            avatar={
              <Avatar src={img} />
            }
            title={title}
          />
          <h4>{content}</h4>
        </Card>

 
        )
}