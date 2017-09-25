import * as React from 'react'
import {connect} from 'react-redux'
import {bindActionCreators} from 'redux'

import * as actionCreators from '@src/actions.ts'


class {{container_name}}Component extends React.Component<any, any> {
    render() {
        return (
            <div/>
        )
    }
}

const mapStateToProps = (state, ownProps) => {
    return {
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        actions: bindActionCreators<any>(actionCreators, dispatch),
    }
}
export const {{container_name}} = connect(
    mapStateToProps,
    mapDispatchToProps
)({{container_name}}Component)
