import React, { Fragment } from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import LandingPage from './Pages/Landing';
export default function router() {
    return (
        <Fragment>
            <Router>
                <Switch>
                    <Route path='/' exact component={LandingPage} />
                    <Route path='/:query/:page' component={LandingPage} />
                </Switch>
            </Router>
        </Fragment>

    )
}