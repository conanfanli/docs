import * as React from 'react'
import {connect} from 'react-redux'
import {bindActionCreators} from 'redux'

import {ACTIONS as actionCreators} from '@src/actions.ts'
import {ActionType} from "@src/types"


interface PropsFromStore {}
interface Prop extends PropsFromStore {}


class {{container_name}}Component extends React.Component<Prop, any> {
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
export const {{container_name}} = connect<PropsFromStore, {actions: ActionType}>(
    mapStateToProps,
    mapDispatchToProps
)({{container_name}}Component)
