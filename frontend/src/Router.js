import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import LandingPage from './pages/Landing';

export default function AppRouter() {
    return (
        <Router>
            <Switch>
                <Route path='/' exact component={LandingPage} />
                <Route path='/:query/:page' component={LandingPage} />
            </Switch>
        </Router>
    );
}
