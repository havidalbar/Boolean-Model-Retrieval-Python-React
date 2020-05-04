import React, { useState, useEffect, Fragment } from 'react';
import { Layout, Input, Col, Row, Pagination, List, Avatar, Modal, Button } from 'antd';
import { motion } from "framer-motion";
import Axios from 'axios';
import Card from '../Component/Card';


function getWindowDimensions() {
    const { innerHeight: height } = window;
    return height
}

async function showDetail(slug){
    let { data } = await Axios.get(`http://localhost/api/detail/${slug}`);
    Modal.info({
        icon:([]),
        style:{top:20},
        width:'70vw',
        content: (
          <div >
          <div style={{textAlign:'center'}}>
          <h3>{data.data.title}</h3>
          <img src={data.data.img} style={{width:'50vh',height:'30vh'}}/>
          </div>
            <p>{data.data.content}</p>
          </div>
        ),
        onOk() {},
      });
    }

export default function Landing(props) {
    const [page, setPage] = useState(props.match.params.page);
    const { Search } = Input;
    const [height, setHeight] = useState(getWindowDimensions())
    const [xValue, SetXValue] = useState(height * 50 / 100);
    const [data, setData] = useState(null);
    const [query, setQuery] = useState(props.match.params.query);
    const [searchValue, setSearchValue] = useState('');
    async function getQuery(value, page) {
        let { data } = await Axios.get(`http://localhost/api/search?q=${value}&page=${page}&limit=8`);
        if (data.data.length != 0) {
            setData(data);
        }
    }

    useEffect(() => {
        function handleResize() {
            setHeight(getWindowDimensions());
        }
        window.addEventListener('resize', handleResize);
        return () => window.removeEventListener('resize', handleResize);
    }, []);

    useEffect(() => {
        if (!props.match.params.page) {
            setPage(1);
        }
        setSearchValue(props.match.params.query);
        getQuery(query, page);
    }, [query, page])

    useEffect(() => {
        if (data) {
            SetXValue(height * 1.5 / 100);
        }
    }, [data]);


    return (
        <div>
            <motion.div
                style={{ flex: 1, width: '100%' }}
                animate={{
                    y: xValue,
                    scale: 1,
                }}
                transition={{ type: 'spring', stiffness: 50 }}
            >
                <Row>
                    <Col xs={2} sm={4} md={6} lg={8} ></Col>
                    <Col xs={20} sm={16} md={12} lg={8} >
                        <Search
                            placeholder="Cari gejala disini"
                            enterButton="Search"
                            size="large"
                            value={searchValue}
                            onChange={value => {
                                setSearchValue(value.target.value);
                            }}
                            onSearch={value => {
                                setQuery(value);
                                SetXValue(height * 1.5 / 100);
                                props.history.push(`/${value}/${page}`)
                            }}
                            autoFocus
                        /></Col>
                    <Col xs={2} sm={4} md={6} lg={8} ></Col>
                </Row>
            </motion.div>
            {data ?
                <div style={{ display: 'flex', marginTop: '2vw' }}>
                    <Row>
                        <Col xs={2} sm={4} md={6} lg={4} ></Col>
                        <Col xs={20} sm={16} md={12} lg={16} >
                            <div style={{
                                display: 'flex',
                                alignItems: 'center',
                                flexDirection: 'column'
                            }}>
                                <List
                                    itemLayout="horizontal"
                                    dataSource={data.data}
                                    renderItem={item => (
                                        <List.Item>
                                            <List.Item.Meta
                                                avatar={<Avatar src={item.img} />}
                                                title={<a onClick={() => showDetail(item.slug)}>{item.title}</a>}
                                                description={item.summary}
                                            />
                                        </List.Item>
                                    )}
                                />
                                <Pagination {...data.meta} defaultCurrent={page} showSizeChanger={false} onChange={(page, pageSize) => {
                                    setPage(page + 1);
                                    document.body.scrollTop = 0; // For Safari
                                    document.documentElement.scrollTop = 0;
                                    props.history.push(`/${query}/${page}`)
                                }} />
                            </div>

                        </Col>
                        <Col xs={2} sm={4} md={6} lg={4} ></Col>
                    </Row>
                </div> : <Fragment />}
        </div>
    )
}
